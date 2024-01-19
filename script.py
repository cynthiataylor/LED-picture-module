import os
import subprocess

base_path = os.getcwd()
print('base_path', base_path)

# TODO: this might need to be 'python3' in some cases
python_executable = 'python'
print('python_executable', python_executable)

py_file_list = []
for dir_path, _, file_name_list in os.walk(base_path):
    for file_name in file_name_list:
        if file_name.endswith('.py'):
            # add full path, not just file_name
            py_file_list.append(
                os.path.join(dir_path, file_name))

print('PY files that were found:')
for i, file_path in enumerate(py_file_list):
    print('   {:3d} {}'.format(i, file_path))

    # call script
    subprocess.run([python_executable, file_path])