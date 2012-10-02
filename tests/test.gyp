{
  'includes': [ '../common.gyp' ],

  'targets': [{
    'target_name': 'test',
    'type': 'executable',
    'include_dirs': [
      '../src/'
    ],
    'libraries' : ['-lv4l1', '-lfg2'],
    'cflags': ['-Wall', '-Wno-unused-parameter',
               '-fPIC', '-fno-strict-aliasing', '-fno-exceptions',
               '-pedantic'],
    'sources': [
 	'test.c',
    ],
  }]
}
