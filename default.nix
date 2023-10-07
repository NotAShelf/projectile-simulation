{
  lib,
  python3Packages,
  doCheck ? true,
  ...
}:
python3Packages.buildPythonApplication {
  pname = "projectile-simulation";
  version = "0.0.1";

  src = ./.;

  propagatedBuildInputs = with python3Packages; [
    numpy
    matplotlib
    pytest
  ];

  nativeCheckInputs = [
    python3Packages.pytest
  ];

  checkPhase = lib.optionals doCheck ''
    runHook preCheck
    pytest
    runHook postCheck
  '';

  meta = {
    description = "Simulate the motion of a projectile with air resistance";
    longDescription = ''
      This is a Python package that simulates the motion of a projectile with air resistance.
      It is based on the Euler method.
    '';
    license = lib.licenses.eupl12;
    maintainers = with lib.maintainers; [NotAShelf];
  };
}
