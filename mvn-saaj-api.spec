#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-saaj-api
Version  : 1
Release  : 2
URL      : https://repo.maven.apache.org/maven2/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5-sources.jar
Source0  : https://repo.maven.apache.org/maven2/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5-sources.jar
Source1  : https://repo.maven.apache.org/maven2/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.jar
Source2  : https://repo.maven.apache.org/maven2/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.1 GPL-2.0-only
Requires: mvn-saaj-api-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-saaj-api package.
Group: Data

%description data
data components for the mvn-saaj-api package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5-sources.jar
/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.jar
/usr/share/java/.m2/repository/javax/xml/soap/saaj-api/1.3.5/saaj-api-1.3.5.pom
