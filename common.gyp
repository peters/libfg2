{
  'variables': {
    'variables': {
      'host_arch%':
        '<!(uname -m | sed -e "s/i.86/ia32/;\
          s/x86_64/x64/;s/amd64/x64/;s/arm.*/arm/;s/mips.*/mips/")',
    },
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'type' : 'shared_library',
    'configurations': {
      'Debug': {
        'cflags': [ '-g', '-O0' ],
	'defines': ['DEBUG=1']
      },
      'Release': {
        'cflags': [ '-O3' ]
      }
    }
  }
}
