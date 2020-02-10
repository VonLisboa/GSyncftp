import asyncio
import glob
import os

import aioftp as aioftp
from PyQt5.QtCore import pyqtSignal, QObject


class UploadFiles(QObject):
    filename_list = "files.list"
    files_list = []
    files_error = []
    files = pyqtSignal(object)
    task_count = 0

    def __init__(self, path_sync, path_folder):
        QObject.__init__(self)
        self.path_sync = path_sync
        self.path = path_folder
        # self.files_list = open(self.filename_list, 'a+')

    def map_files(self, path, count=0):
        path = path + os.sep

        # only files
        for file in sorted(glob.glob(path + '*.*'), key=os.path.getsize):
            self.files_list.append(file)
            # count += 1
            # self.files_list.write(f"{file}{count}\n")

        # only folders - recursively for each subfolder
        for folder in sorted(glob.glob(path + '**/'), key=os.path.getsize):
            self.map_files(folder[:-1])
            # count = self.map_files(folder[:-1], count)
            # count += 1
        # return count

    @asyncio.coroutine
    async def __async_upload(self, file_path):
        try:
            file_dest = file_path.replace(self.path_sync, "").replace(os.environ["HOMEDRIVE"]+os.sep, "").replace("\\", '/')
            async with aioftp.ClientSession("host", 21, "user", "pass") as client:
                if not await client.exists(file_dest.split('/')[1]):
                    try:
                        await client.make_directory(file_dest.split('/')[1])
                    except:
                        pass

                if not await client.exists(file_dest):
                    await client.upload(file_path, file_dest, write_into=True)
                    self.files_list.remove(file_path)
                    self.files.emit(self.files_list)
                else:
                    self.files_list.remove(file_path)
                    self.files.emit(self.files_list)
                    # verificar se o arquivo é mais recente e então fazer o upload
                    pass

        except Exception as e:
            self.files_error.append(file_path)
            print(e)

    @asyncio.coroutine
    async def __async_run(self):
        tasks = []
        files_p = self.files_list.copy()
        total = len(files_p)
        while total > 0:
            tasks.append(self.loop.create_task(self.__async_upload(files_p.pop(0))))
            if len(tasks) == 4:
                await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                tasks = []
            total = len(files_p)

        if len(tasks) > 0:
            await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

        if len(self.files_error) > 0:
            self.files_list = self.files_error.copy()
            self.files_error = []
            await self.__async_run()
        # asyncio.get_event_loop().close()
        # self.loop.close()
        return

    def run(self):
        try:
            self.map_files(self.path)
            # self.files.emit(self.files_list)
            # dando problema de crash, funciona dentro de thread
            self.loop = asyncio.new_event_loop()
            self.loop.run_until_complete(self.__async_run())
        except Exception as e:
            print(e)


"""
up = UploadFiles()
up.map_files("C:\\Users\\glaucio\\Pictures")
up.test()
"""
