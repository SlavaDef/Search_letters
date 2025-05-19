log_file = 'vsearch.log'
directory = 'cati_666.txt'
dbconfig = {'host': '127.0.0.1',
           'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',
            }

log_file2 = 'webapp/vsearch.log'
file_from_pc = 'C:/Users/Admin/PycharmProjects/keyes/key_for_login_in_vsearch.txt'


_SQL = """show tables"""
_SQL2 = """describe log"""
SQL3 = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)""" # сюди будуть приходити данні від методу
SQL4 = """select * from log"""
