detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        "Ubuntu")
            install_linux
            ;;
        *)
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}
install_linux(){
    sudo echo "sudo python $HOME/.dx4/installerpy/main.py \$1 \$2 \$3 \$4 \$5" > $HOME/.local/bin/installerpy
    sudo mkdir -p $HOME/.dx4
    sudo echo 'echo "[*] Uninstalling installerpy..." && sudo rm -rf $HOME/.dx4/installerpy && sudo rm -rf $HOME/.local/bin/installerpy && sudo rm -rf $HOME/.local/bin/installerpy-uninstaller && echo "[*] installerpy uninstall task done"' > $HOME/.local/bin/installerpy-uninstaller
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.dx4/installerpy"
    sudo chmod +x $HOME/.local/bin/installerpy
    sudo chmod +x $HOME/.local/bin/installerpy-uninstaller
}
install_termux(){
    mkdir -p $HOME/.dx4
    cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.dx4/installerpy"
    echo "python $HOME/.dx4/installerpy/main.py \$1 \$2 \$3 \$4 \$5" > $PREFIX/bin/installerpy
    echo 'echo "[*] Uninstalling installerpy..." && rm -rf $HOME/.dx4/installerpy && rm -rf $PREFIX/bin/installerpy && rm -rf $PREFIX/bin/installerpy-uninstaller && echo "[*] installerpy uninstall task done"' > $PREFIX/bin/installerpy-uninstaller
    chmod +x $PREFIX/bin/installerpy
    chmod +x $PREFIX/bin/installerpy-uninstaller
}
detect_platform