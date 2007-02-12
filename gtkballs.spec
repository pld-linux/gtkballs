Summary:	Simple logic game
Summary(fr.UTF-8):   Un simple jeu de logique
Summary(pl.UTF-8):   Prosta gra logiczna
Summary(ru.UTF-8):   Простая и увлекательная логическая игра
Name:		gtkballs
Version:	3.1.5
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gtkballs.antex.ru/dist/%{name}-%{version}.tar.gz
# Source0-md5:	1654799db1e9a46607b06f7ad3c0bf05
Source1:	%{name}.desktop
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

%description -l fr.UTF-8
GtkBalls est un simple jeu de logique. Le but du jeu est de faire le
nombre maximum de lignes avec des balles de la même couleur. Une ligne
est constituée de cinq balles. A chaque fois que vous ne faites pas
une ligne, des balles suplémentaires apparaissent sur la grille. Vous
perdez lorsque la grille est pleine.

%description -l pl.UTF-8
Celem gry jest zdobycie jak największej liczby punktów poprzez
ustawianie piłek tego samego koloru w poziomych, pionowych bądź
ukośnych liniach.

%description -l ru.UTF-8
GtkBalls -- это простая логическая игра. Цель игры -- составлять
линии максимальной длины из шариков одинакового цвета. Минимальная
длина линии за которую дают очки -- 5 шариков. Если вы не составили
линию за ход, то на следуюем ходу появляются новые шарики. Игра
заканчивается, когда на поле не остается места для новых шариков.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/COPYING

install gnome-gtkballs.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/*.desktop
%{_pixmapsdir}
