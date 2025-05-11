from utils.constants import directory, log_file
from markupsafe import escape


def view_logs(): # my_version of logs
    res=[]
    with open(directory) as file:
        read_all = file.readlines()
        for line in read_all:
            res.append(line.split("*"))
    return res


def view_logs2(): # olso works without read_all
    res=[]
    with open(directory) as file:
        for line in file:
            res.append(line.split("*"))
    return res



def view_logs3():# gpt version
    with open(directory) as file:
        return [line.split("*") for line in file]



def view_the_logs2(): # gpt version
    with open(log_file) as log:
        contents = [
            [escape(item) for item in line.split("***")]
            for line in log
        ]
    return contents


def view_the_logs33(): # book version with render_template
    contents = []
    with open(log_file) as log:
        for line in log:
           contents.append([])
           for item in line.split("***"):
               contents[-1].append(escape(item))
    return contents
    #return render_template('logs.html', log_data=view_the_logs2(), the_title='View logs')



