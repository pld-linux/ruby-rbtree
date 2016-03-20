%define pkgname rbtree
Summary:	Ruby/RBTree
Name:		ruby-%{pkgname}
Version:	0.4.2
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	096e8561315e2c382405369391510b93
URL:		http://rbtree.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RBTree is a sorted associative collection that is implemented with
Red-Black Tree. The elements of RBTree are ordered and its interface
is the almost same as Hash, so simply you can consider RBTree sorted
Hash.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__ruby} extconf.rb \
	--vendor

%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README test.rb
%attr(755,root,root) %{ruby_vendorarchdir}/rbtree.so
