#
# spec file for package perl-FFI-C (Version 0.15)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name FFI-C
Name:           perl-FFI-C
Version:        0.15
Release:        0
%define debug_package %{nil}
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        C data types for FFI
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(FFI::Platypus) >= 1.24
BuildRequires:  perl(FFI::Platypus::Memory)
BuildRequires:  perl(FFI::Platypus::Record)
BuildRequires:  perl(FFI::Platypus::Type::Enum) >= 0.03
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Sub::Identify) >= 0.05
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::V0) >= 0.000081
Requires:       perl(Class::Inspector)
Requires:       perl(FFI::Platypus) >= 1.24
Requires:       perl(FFI::Platypus::Memory)
Requires:       perl(FFI::Platypus::Type::Enum) >= 0.03
Requires:       perl(Ref::Util)
Requires:       perl(Sub::Identify) >= 0.05
Requires:       perl(Sub::Install)
Requires:       perl(Sub::Util)
%{?perl_requires}

%description
This distribution provides tools for building classes to interface for
common C data types. Arrays, 'struct', 'union' and nested types based on
those are supported.

Core FFI::Platypus also provides FFI::Platypus::Record for manipulating and
passing structured data. Typically you want to use FFI::C instead, the main
exception is when you need to pass structured data by value instead of by
reference.

To work with C APIs that work with C file pointers you can use FFI::C::File
and FFI::C::PosixFile. For C APIs that expose the POSIX 'stat' structure
use FFI::C::Stat.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
