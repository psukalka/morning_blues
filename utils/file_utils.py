import os


def get_size_of_dir(base_path):
    """
    Utility to return size of a directory. It sums only the sizes of files in a directory.
    Reference: https://stackoverflow.com/a/1392549
    :param base_path: Path of base directory
    :return:
    """
    if base_path is None:
        return 0
    total_size = 0
    for dirpath, _, filenames in os.walk(base_path):
        for f_name in filenames:
            fp = os.path.join(dirpath, f_name)
            if not os.path.islink(fp):
                # print("file_name: {} , size: {}".format(fp, os.path.getsize(fp)))
                total_size += os.path.getsize(fp)
    return total_size


print(get_size_of_dir("/Users/pavansukalkar/Desktop/repositories/test"))