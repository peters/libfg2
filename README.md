libfg2 - Simple Linux Video Capture Library
===========================================

Introduction
------------

Created by Matthew Brush ([codebrainz/libfg2](https://github.com/codebrainz/libfg2)). The reason for the fork was to remove
some unnecessary dependencies. The build system has also been replaced with gyp.

Libfg2 is a C library which provides access to video input devices such as
frame grabber cards, webcams, and TV tuner devices under kernels which support
Video4Linux2.  Using the excellent libv4l library, libfg2 provides access to
most devices, independent of which pixel formats they use.  

Example (Snapshot from webcamera)
-------

Here's a minimal example of use:

```c
#include <libfg2.h>

int main(int argc, char *argv[])
{

    /* get name of video device or default */
    char *device = (argc>1) ? argv[1] : "/dev/video0";

    /* get name of snapshot file or default */
    char *snap_file = (argc>2) ? argv[2] : "snapshot.jpg";

    /* open and initialize the fg_grabber */
    fg_grabber *fg = fg_open(device);

    /* allocate a new fg_frame and fill it with data */
    fg_frame *fr = fg_grab(fg);

    /* save the fg_frame as a JPEG */
    fg_frame_save(fr, snap_file);

    /* free memory for fg_frame */
    fg_frame_release(fr);

    /* free memory for fg_grabber and close device */
    fg_close(fg);

    return 0;
}
```

You can compile the example using:

    $ gcc -o webcam-snapshot example.c -lfg2 -lv4l2 -ljpeg -Isrc
    $ ./webcam-snapshot /dev/video0

Running the test suite 
----------------------

    $ make test


Build dependencies (Ubuntu 12.04)
---------------------------

    $ sudo apt-get install libv4l-dev libjpeg-dev gyp

Building and Installing (Ubuntu 12.04)
-------------------------------------

To checkout, build and install libfg2 you'll need to do the following:

    $ git clone git://github.com/codebrainz/libfg2.git
    $ cd libfg2
    $ make
    $ cp libfg2.so /usr/local/lib
    $ sudo ldconfig

LICENSE
-------
Libfg2 is licensed under the
[GNU Lesser General Public License](http://www.gnu.org/copyleft/lesser.html),
see the
[LICENSE file](https://github.com/peters/libfg2/blob/master/LICENSE).
