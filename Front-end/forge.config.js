module.exports = {
  packagerConfig: {
    icon: './logoo.png',

  },
  rebuildConfig: {},
  makers: [
    {
      name: '@electron-forge/maker-squirrel',
      config: {
        setupIcon: './logoo.png'
      },
    
    },
    {
      name: '@electron-forge/maker-zip',
      platforms: ['darwin'],
    },
    {
      name: '@electron-forge/maker-deb',
      config: {
        options: {
          icon: './logoo.png',
        },
      },
    },
    {
      name: '@electron-forge/maker-rpm',
      config: {
        icon: './logoo.png',
      },
    },
  ],
};
