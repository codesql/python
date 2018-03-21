#kl:rocksdb backup test
import rocksdb
import sys, getopt,os


def main(argv):
    inputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hd:o:",["database="])
    except getopt.GetoptError:
      print 'rocksdb_backup.py -d database_name [e]'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'rocksdb_backup.py -d database_name '
         sys.exit()
      elif opt in ("-d", "--database"):
         inputfile = arg
         print 'Database to be backed up', inputfile
         db = rocksdb.DB(inputfile, rocksdb.Options(create_if_missing=False))
         backup = rocksdb.BackupEngine("./backups.bk")
         backup.create_backup(db, flush_before_backup=True)
         print 'Database ', inputfile, ' has been successfully backed up ', os.getcwd(), '/backups.bk'
      else:
         assert False, "Invalid Options"
if __name__ == "__main__":
   main(sys.argv[1:])
