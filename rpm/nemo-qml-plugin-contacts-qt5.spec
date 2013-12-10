# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugin-contacts-qt5

# >> macros
# << macros

Summary:    Nemo QML contacts plugin
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-contacts
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-contacts-qt5.yaml
Requires:   qtcontacts-sqlite-qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Contacts)
BuildRequires:  pkgconfig(Qt5Versit)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(qtcontacts-sqlite-qt5-extensions) >= 0.1.27
BuildRequires:  pkgconfig(contactcache-qt5) >= 0.0.50
BuildRequires:  pkgconfig(mlocale5)

%description
%{summary}.

%package tools
Summary:    Development tools for qmlcontacts
License:    BSD
Group:      Applications/System
Provides:   qmlcontacts-tools > 0.4.9
Obsoletes:  qmlcontacts-tools <= 0.4.9

%description tools
%{summary}.

%package tests
Summary:    QML contacts plugin tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/contacts/libnemocontacts.so
%{_libdir}/qt5/qml/org/nemomobile/contacts/qmldir
# >> files
# << files

%files tools
%defattr(-,root,root,-)
%{_bindir}/vcardconverter
# >> files tools
# << files tools

%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins-qt5/contacts/*
# >> files tests
# << files tests
