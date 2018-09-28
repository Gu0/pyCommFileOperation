'''二进制文件操作库'''


def read_bytes_from_file(path, pos, length):
    '''读取二进制文件指定位置内容，输出bytes内容'''
    with open(path, 'rb') as f:
        f.seek(pos)
        contents = f.read(length)
    assert(len(contents) == length)
    return contents


def write_bytes_to_file(path, pos, data):
    '''将bytes写入到二进制文件指定位置'''
    with open(path, 'rb') as f:
        contents = f.read()
    # 替换对应位置的数据
    length = len(data)
    new_contents = contents[0:pos] + data + contents[(pos+length):]
    with open(path, 'wb') as f:
        f.write(new_contents)
