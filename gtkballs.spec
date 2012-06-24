Summary:	Simple logic game
Summary(fr):	Un simple jeu de logique
Summary(pl):	Prosta gra logiczna
Summary(ru):	������� � ������������� ���������� ����
Name:		gtkballs
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Vendor:		Sergey Pinaev <dfo@antex.ru>
Source0:	ftp://ftp.antex.ru/pub/unix/dfo/gtkballs/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://gtkballs.antex.ru/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%patch0 -p1

%build
aclocal
autoconf
autoheader
automake -a -f
%configure --localstatedir=%{_localstatedir}/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING

ln -s %{_datadir}/%{name} $RPM_BUILD_ROOT%{_pixmapsdir}
install gnome-gtkballs.png $RPM_BUILD_ROOT%{_pixmapsdir}
install GtkBalls.desktop $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf README ChangeLog NEWS README.russian TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,games) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%attr(666,root,games) %{_localstatedir}/games/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
