# http://github.com/hashicorp/hcl

%global goipath         github.com/hashicorp/hcl
%global commit          ef8133da8cda503718a74741312bf50821e6de79


%gometa -i

Name:           %{goname}
Version:        0
Release:        0.17%{?dist}
Summary:        HCL is a configuration language
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/davecgh/go-spew/spew)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
#test-fixtures
files="find . -iname 'test-fixtures' -type d) find . -iname 'testdata' -type d)"
%goinstall glide.lock glide.yaml $files

%check
%gochecks -d hcl/ast -d hcl/fmtcmd

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.gitef8133d
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20161116gitef8133d
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitef8133d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.gitef8133d
- Bump to upstream ef8133da8cda503718a74741312bf50821e6de79
  related: #1250468

* Thu Jan 12 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git2deb1d1
- Polish the spec file
  related: #1250468

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git2deb1d1
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2deb1d1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git2deb1d1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 jchaloup <jchaloup@redhat.com> - 0-0.5.git2deb1d1
- Copy missing directories with test data and run removed tests
  related: #1250468

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.git2deb1d1
- Bump to upstream 2deb1d1db27ed473f38fe65a16044572b9ff9d30
  Removed deleted tests
  related: #1250468

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git513e04c
- Update to spec-2.1
  related: #1250468

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git513e04c
- Update spec file to spec-2.0
  resolves: #1250468

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git513e04c
- First package for Fedora
  resolves: #1212059

