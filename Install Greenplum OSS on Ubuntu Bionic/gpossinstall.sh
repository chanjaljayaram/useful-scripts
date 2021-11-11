sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:greenplum/db -y
sudo apt-get update -y
sudo apt-get install greenplum-db-6 -y
source /opt/greenplum-db-*/greenplum_path.sh
cp $GPHOME/docs/cli_help/gpconfigs/gpinitsystem_singlenode .
hostname > hostlist_singlenode
mkdir primary master
sed -i "s|/gpdata1|$(pwd)/primary|g" gpinitsystem_singlenode
sed -i "s|/gpdata2|$(pwd)/primary|g" gpinitsystem_singlenode
sed -i "s|MASTER_HOSTNAME=hostname_of_machine|MASTER_HOSTNAME=$(hostname)|g" gpinitsystem_singlenode
sed -i "s|/gpmaster|$(pwd)/master|g" gpinitsystem_singlenode
gpssh-exkeys -f hostlist_singlenode
gpinitsystem -c gpinitsystem_singlenode -a