{
  'includes': [ 'common.gyp' ],

  'targets': [{
    'target_name': 'libfg2',
    'type': 'shared_library',
    'include_dirs': [
      'include',
      'src/'
    ],
    'defines' : ['WITH_LIBV4L=1', 'WITH_JPEG=1'],
    'libraries' : ['-lv4l1', '-ljpeg'],
    'cflags': ['-Wall', '-Wno-unused-parameter',
               '-fPIC', '-fno-strict-aliasing', '-fno-exceptions',
               '-pedantic'],
    'sources': [
 	'src/libfg2.h',
	'src/control.c',
	'src/frame.c',
	'src/capture.c',
	'src/convert.c'
    ],
  }]
}