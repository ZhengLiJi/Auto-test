import os


class FilePath:
    BasePath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # print(BasePath)
    LogPath = os.path.join(BasePath, "log")
    # print(LogPath)
    ReportPath = os.path.join(BasePath, "report")
    # print(ReportPath)


if __name__ == '__main__':
    print(FilePath.BasePath)
