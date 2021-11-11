# Convert data from a Greenplum/Postgres database to parquet files using Python

## Python libraries used
- psycopg2
- pandas
- pyarrow
- argparse
- pyarrow.parquet

## Sample invocation of the script
```sh
$ python psql2parquet.py --file <file-containing-table-list> --output <directory-where-output-files-are-stored> --dbname <db-name> --dbuser <db-username> --dbpassword <db-password> --dbhost <db-hostname-or-ip> --dbport <db-port>
```
