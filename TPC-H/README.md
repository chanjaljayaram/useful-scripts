# TPC-H generate sample data (from Ubuntu)
- Unzip the file
- Copy TPC-H_Tools_v3.0.0/dbgen/makefile.suite to TPC-H_Tools_v3.0.0/dbgen/makefile
- Make following updates
    ```sh
    CC      = gcc
    DATABASE= ORACLE
    MACHINE = LINUX
    WORKLOAD = TPCH
    ```
- Compile
    ```sh
    make
    ```
- Run dbgen to generate csv
    ```sh
    dbgen -s 0.1
    ```
- Remove trailing delimiter | from every line
    ```sh
    for i in `ls *.tbl`; do sed 's/|$//' $i > ${i/tbl/csv}; echo $i; done;
    ```