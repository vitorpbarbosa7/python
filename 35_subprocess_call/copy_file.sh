site_packages=$(python3 -c "import setuptools as _; print(_.__path__[0])")

echo site package location is: [[$site_packages]]

project_name=myproject

echo project_name is: [[$project_name]]

string_copy_file="cp entrypoint.sh '$site_packages/$project_name'"
echo String to copy files is: [[$string_copy_file]]

eval $string_copy_file
