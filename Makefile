BUILDTYPE ?= Debug
JOBS ?= 1
ARCH ?=

all: libfg2.so

build:
	gyp --generator-output=build --format=make --depth=. libfg2.gyp tests/test.gyp

libfg2.so: build
	$(MAKE) -j $(JOBS) -C build libfg2
	ln -sf build/out/$(BUILDTYPE)/lib.target/libfg2.so libfg2.so

test: build
	tests/test

clean:
	-rm -rf build
	-rm libfg2.so

.PHONY: clean all build test libfg2.so
