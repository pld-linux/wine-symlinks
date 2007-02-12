# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).

%define _wine_cdrive	%{_datadir}/wine

Summary:	Meta-package to create links to WINE replacements of Windows programs
Summary(pl.UTF-8):   Metapakiet tworzący dowiązania do odpowiedników programów Windows zawartych w WINE
Name:		wine-symlinks
Version:	1.0
Release:	10
Group:		Applications/Emulators
License:	LGPL
Requires:	wine
#Requires:	wine-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides symlinks from /usr/lib/wine/*.exe* to /var/lib/wine/windows -
the standard place for WINE's C drive. This allows software installed
with WINE to take advantage of WINE's replacements of common Windows
utilities.

%description -l pl.UTF-8
Pakiet ten zawiera dowiązania symboliczne z /usr/lib/wine/*.exe* do
/var/lib/wine/windows - standardowej lokalizacji dysku C WINE.
Umożliwia to wykorzystanie zawartych w WINE odpowiedników podstawowych
programów narzędziowych Windows przez programy zainstalowane pod WINE.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wine_cdrive}/windows/command
install -d $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system
install -d $RPM_BUILD_ROOT%{_wine_cdrive}/windows/desktop
install -d $RPM_BUILD_ROOT%{_wine_cdrive}/wine
# boring windows stuff.
ln -s %{_libdir}/wine/aviinfo.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/aviinfo.exe
ln -s %{_libdir}/wine/aviplay.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/aviplay.exe
ln -s %{_libdir}/wine/clock.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/clock.exe
ln -s %{_libdir}/wine/control.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/control.exe
ln -s %{_libdir}/wine/expand.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/expand.exe
ln -s %{_libdir}/wine/icinfo.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/icinfo.exe
ln -s %{_libdir}/wine/notepad.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/notepad.exe
ln -s %{_libdir}/wine/progman.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/progman.exe
ln -s %{_libdir}/wine/regapi.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/regapi.exe
ln -s %{_libdir}/wine/regedit.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/regedit.exe
ln -s %{_libdir}/wine/rundll32.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/rundll32.exe
ln -s %{_libdir}/wine/start.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/command/start.exe
ln -s %{_libdir}/wine/winefile.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/fileman.exe
ln -s %{_libdir}/wine/winemine.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/winmine.exe
ln -s %{_libdir}/wine/winhelp.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/winhelp.exe
ln -s %{_libdir}/wine/winver.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/winver.exe
# system stuff.
ln -s %{_libdir}/wine/gdi.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/gdi.exe
ln -s %{_libdir}/wine/krnl386.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/krnl386.exe
ln -s %{_libdir}/wine/regsvr32.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/regsvr32.exe
#ln -s %{_libdir}/wine/rpcss.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/rpcss.exe
ln -s %{_libdir}/wine/uninstaller.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/uninstaller.exe
ln -s %{_libdir}/wine/user.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/user.exe
ln -s %{_libdir}/wine/wcmd.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/cmd.exe
ln -s %{_libdir}/wine/wineboot.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/windows/system/softboot.exe
# Wine specific stuff.
ln -s %{_libdir}/wine/wineconsole.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/wine/wineconsole.exe
ln -s %{_libdir}/wine/winedbg.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/wine/winedbg.exe
ln -s %{_libdir}/wine/winecfg.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/wine/winecfg.exe
ln -s %{_libdir}/wine/winepath.exe.so $RPM_BUILD_ROOT%{_wine_cdrive}/wine/winepath.exe
ln -s %{_prefix}/X11R6/lib/X11/fonts/TTF $RPM_BUILD_ROOT%{_wine_cdrive}/windows/fonts
ln -s /tmp $RPM_BUILD_ROOT%{_wine_cdrive}/windows/temp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_wine_cdrive}/windows/aviinfo.exe
%{_wine_cdrive}/windows/aviplay.exe
%{_wine_cdrive}/windows/clock.exe
%{_wine_cdrive}/windows/control.exe
%{_wine_cdrive}/windows/expand.exe
%{_wine_cdrive}/windows/icinfo.exe
%{_wine_cdrive}/windows/notepad.exe
%{_wine_cdrive}/windows/progman.exe
%{_wine_cdrive}/windows/regapi.exe
%{_wine_cdrive}/windows/regedit.exe
%{_wine_cdrive}/windows/rundll32.exe
%{_wine_cdrive}/windows/command/start.exe
%{_wine_cdrive}/windows/fileman.exe
%{_wine_cdrive}/windows/winmine.exe
%{_wine_cdrive}/windows/winhelp.exe
%{_wine_cdrive}/windows/winver.exe
%{_wine_cdrive}/windows/system/gdi.exe
%{_wine_cdrive}/windows/system/krnl386.exe
%{_wine_cdrive}/windows/system/regsvr32.exe
#%{_wine_cdrive}/windows/system/rpcss.exe
%{_wine_cdrive}/windows/system/uninstaller.exe
%{_wine_cdrive}/windows/system/user.exe
%{_wine_cdrive}/windows/system/cmd.exe
%{_wine_cdrive}/windows/system/softboot.exe
%{_wine_cdrive}/wine/wineconsole.exe
%{_wine_cdrive}/wine/winedbg.exe
%{_wine_cdrive}/wine/winecfg.exe
%{_wine_cdrive}/wine/winepath.exe
%{_wine_cdrive}/windows/fonts
%{_wine_cdrive}/windows/temp
%{_wine_cdrive}/windows/desktop
