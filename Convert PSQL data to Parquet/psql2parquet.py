import psycopg2,pandas,pyarrow,argparse
import pyarrow.parquet as pq

argParser = argparse.ArgumentParser()
argParser.add_argument("--file", "-f", help="File containing the list of tables and headers.")
argParser.add_argument("--output", "-O", help="Directory where CSVs and Parquet output needs to be saved.")
argParser.add_argument("--dbname", "-d", help="Postgres Database name.")
argParser.add_argument("--dbuser", "-u", help="Postgres Username.")
argParser.add_argument("--dbpassword", "-p", help="Postgres User password.")
argParser.add_argument("--dbhost", "-H", help="Postgres DB host.")
argParser.add_argument("--dbport", "-P", help="Postgres DB port.")

args = argParser.parse_args()

conn = psycopg2.connect(database=args.dbname,user=args.dbuser,password=args.dbpassword,host=args.dbhost,port=args.dbport)
cursor=conn.cursor()

tablesFile = open(args.file,'r')

for table in tablesFile:
  tablename = table.split(',')[0]
  tableheaders= table.split(',')[1].split()
  csvFile = open(args.output+'/'+tablename+'.csv','w')
  cursor.copy_to(csvFile,tablename,sep=',')
  csvFile.close()
  dataFrame=pandas.read_csv(args.output+'/'+tablename+'.csv',sep=",",names=tableheaders,index_col=False)
  arrowTable = pyarrow.Table.from_pandas(dataFrame)
  pq.write_table(arrowTable, args.output+'/'+tablename+'.parquet')

tablesFile.close()
conn.close()
