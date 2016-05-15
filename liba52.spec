Name:           liba52
Version:        0.7.4
Release:        1%{?dist}
Summary:        A free ATSC A/52 stream decoder

License:        GPLv2
URL:            http://liba52.sourceforge.net/
Source0:        http://liba52.sourceforge.net/files/a52dec-%{version}.tar.gz
Patch0:         a52dec-0.7.4-allow-pic.patch

%description
liba52 is a free library for decoding ATSC A/52 streams. It is released under
the terms of the GPL license. The A/52 standard is used in a variety of
applications, including digital television and DVD. It is also known as AC-3.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n a52dec
Summary:        A test program for liba52

%description    -n a52dec
a52dec is a test program for liba52. It decodes ATSC A/52 streams, and also
includes a demultiplexer for mpeg-1 and mpeg-2 program streams.

%prep
%setup -q -n a52dec-%{version}
%patch0 -p1


%build
%configure --disable-static --enable-shared

sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc AUTHORS HISTORY NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc doc/liba52.txt
%{_includedir}/*
%{_libdir}/*.so

%files -n a52dec
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Sun May 15 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.7.4-1
- Public release
