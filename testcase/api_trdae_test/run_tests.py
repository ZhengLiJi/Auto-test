import os
import shutil
import subprocess
import argparse
import pytest
import time

def set_environment(env):
    """设置环境变量"""
    os.environ['env'] = env
    print("设置的环境变量 'env' 的值:", os.environ.get('env'))

def setup_results_directory(env):
    """设置结果目录"""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    results_dir = os.path.join(base_dir, f"results_{env}")
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    return results_dir

def run_pytest(env, results_dir, test_file):
    """运行pytest并生成Allure报告"""
    pytest_args = ["-vs", '--alluredir', results_dir]
    if test_file:
        pytest_args.append(test_file)
    pytest.main(pytest_args)

    # 生成Allure报告
    allure_path = shutil.which("allure")
    subprocess.run([allure_path, "generate", results_dir, "-o", f'D:/Tiki/reports_{env}', "--clean"],
                   check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def run_tests_for_envs(envs, test_file):
    """根据环境列表运行测试"""
    for env in envs:
        print(f"Running tests for environment: {env}")
        set_environment(env)
        results_dir = setup_results_directory(env)
        run_pytest(env, results_dir, test_file)

def main():
    """主函数，解析命令行参数并运行测试"""
    parser = argparse.ArgumentParser(description='运行测试脚本')
    parser.add_argument('--envs', type=str, default="sit", help='逗号分隔的环境名称列表，默认为 "sit"')
    parser.add_argument('--test_file', type=str, default=None, help='指定测试文件的路径')
    args = parser.parse_args()
    envs = args.envs.split(',')
    test_file = args.test_file
    run_tests_for_envs(envs, test_file)

if __name__ == "__main__":
        main()
