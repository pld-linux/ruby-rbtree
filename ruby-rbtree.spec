Summary:	Ruby/RBTree
Name:		ruby-rbtree
Version:	0.3.0
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/67118/rbtree-%{version}.tar.gz
# Source0-md5:	1bb99fba5b15bcfeaae75271c3c60043
URL:		http://raa.ruby-lang.org/project/ruby-rbtree/
Requires:	ruby >= 1:1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RBTree is a sorted associative collection that is implemented with
Red-Black Tree. The elements of RBTree are ordered and its interface
is the almost same as Hash, so simply you can consider RBTree sorted
Hash.

%prep
%setup -qn rbtree-%{version}

%build
%{__ruby} extconf.rb
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
%doc ChangeLog LICENSE README test.rb
%attr(755,root,root) %{ruby_sitearchdir}/rbtree.so
