/**
 * Metro configuration for React Native
 * https://github.com/facebook/react-native
 *
 * @format
 */
const path = require('home/sebu/CyberHead/cyberhead/modules/');

const extraNodeModules = {
  'DataSets': path.resolve(__dirname + 'datasets/javascript/'),
};

const watchFolders = [
  path.resolve(__dirname + 'datasets/javascript/')
];

module.exports = {
  resolver: {
    extraNodeModules,
  },
  watchFolders
};

