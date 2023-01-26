/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.6.6",
};

require('dotenv').config();
require("@nomiclabs/hardhat-ethers");

const { INFURA_URL_ENDPOINT_SEPOLIA, PRIVATE_KEY } = process.env;

module.exports = {
   solidity: "0.8.17",
   defaultNetwork: "sepolia",
   networks: {
      hardhat: {},
      sepolia: {
         url: INFURA_URL_ENDPOINT_SEPOLIA,
         accounts: [`0x${PRIVATE_KEY}`]
      }
   },
}