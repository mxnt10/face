#!/bin/bash

pkgver='1.3'
install_root=${install_root:-""}

set -e
# shellcheck disable=SC2015
[ "$install_root" != "" ] && {
  mkdir -p "$install_root"/usr/{bin,share/{applications,pixmaps,face/icon_status},doc/face-"$pkgver"}
} || {
  mkdir -p /usr/{share/face/icon_status,doc/face-"$pkgver"}
}

install -Dm 0644 appdata/face.svg "$install_root"/usr/share/pixmaps
install -Dm 0644 appdata/face.desktop "$install_root"/usr/share/applications
install -Dm 0644 icon_status/* "$install_root"/usr/share/face/icon_status

cp -a ChangeLog LICENSE README.md "$install_root"/usr/doc/face-"$pkgver"
cp -Tr src "$install_root"/usr/share/face

echo "#!/bin/bash
cd /usr/share/face
python3 face.py" > "$install_root"/usr/bin/face

chmod 755 "$install_root"/usr/bin/face
exit 0
