{
  'includes': [ 'common.gyp' ],

  'targets': [{
    'target_name': 'libfg2',
    'type': 'shared_library',
    'include_dirs': [
      'include',
      'src/'
    ],
    'defines' : ['WITH_LIBV4L=1', 'WITH_JPEG=1','HAVE_CONFIG_H=1'],
    'libraries' : ['-lv4l1', '-ljpeg'],
    'cflags': ['-Wall', '-Wno-unused-parameter',
               '-fPIC', '-fno-strict-aliasing', '-fno-exceptions', '-fno-tree-vrp'],
    'sources': [
 	'src/libfg2.h',
	'src/control.c',
	'src/frame.c',
	'src/capture.c',
	'src/convert.c'
    ],
  }]
}
