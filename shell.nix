{pkgs, ...}: let
  my-python-packages = ps:
    with ps; [
      matplotlib
      numpy
    ];
  my-python = pkgs.python3.withPackages my-python-packages;
in
  my-python.env
