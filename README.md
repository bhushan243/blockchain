# blockchain

sudo docker build --tag smartcontract .
sudo docker pull bhushan243/blockchain:smartcontract
sudo docker run -p 8090:8080 --name smartcontract1 -d bhushan243/blockchain:smartcontract
