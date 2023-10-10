{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = {
    self,
    nixpkgs,
  }: let
    systems = ["x86_64-linux" "aarch64-linux"];
    forEachSystem = nixpkgs.lib.genAttrs systems;

    pkgsForEach = nixpkgs.legacyPackages;
  in {
    packages = forEachSystem (system: {
      default = self.packages.${system}.projectile-simulation;
      projectile-simulation = pkgsForEach.${system}.callPackage ./default.nix {};
    });

    devShells = forEachSystem (system: {
      devShells = {
        default = self.devShells.${system}.python-shell;
        python-shell = pkgsForEach.${system}.callPackage ./shell.nix {};
      };
    });
  };
}
