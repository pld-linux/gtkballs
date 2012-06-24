Summary:	Simple logic game
Summary(fr):	Un simple jeu de logique
Summary(pl):	Prosta gra logiczna
Summary(ru):	������� � ������������� ���������� ����
Name:		gtkballs
Version:	3.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.antex.ru/pub/unix/dfo/gtkballs/%{name}-%{version}.tar.gz
# Source0-md5:	0f9997110518460db508af353f6324c2
Patch1:		%{name}2-desktop.patch
URL:		http://gtkballs.antex.ru/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
The goal of this game is to make the highest score by matching a
number of balls of the same color in a horizontal, vertical or
diagonal line.

%description -l fr
GtkBalls est un simple jeu de logique. Le but du jeu est de faire le
nombre maximum de lignes avec des balles de la m�me couleur. Une ligne
est constitu�e de cinq balles. A chaque fois que vous ne faites pas
une ligne, des balles supl�mentaires apparaissent sur la grille. Vous
perdez lorsque la grille est pleine.

%description -l pl
Celem gry jest zdobycie jak najwi�kszej liczby punkt�w poprzez
ustawianie pi�ek tego samego koloru w poziomych, pionowych b�d�
uko�nych liniach.

%description -l ru
GtkBalls -- ��� ������� ���������� ����.  ���� ���� -- ����������
����� ������������ ����� �� ������� ����������� �����.  �����������
����� ����� �� ������� ���� ���� -- 5 �������.  ���� �� �� ���������
����� �� ���, �� �� �������� ���� ���������� ����� ������.  ����
�������������, ����� �� ���� �� �������� ����� ��� ����� �������.

%prep
%setup -q
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--localstatedir=%{_localstatedir}/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING

ln -s %{_datadir}/%{name} $RPM_BUILD_ROOT%{_pixmapsdir}
install gnome-gtkballs.png $RPM_BUILD_ROOT%{_pixmapsdir}
install GtkBalls.desktop $RPM_BUILD_ROOT%{_applnkdir}/Games

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS README.russian TODO
%attr(755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%attr(666,root,games) %{_localstatedir}/games/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
