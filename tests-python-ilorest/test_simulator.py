import redfish
import json
import os

# Connection details for the mock-server simulator / 模拟器连接详情
SYSTEM_URL = "https://127.0.0.1:5000"
LOGIN_ACCOUNT = "admin"
LOGIN_PASSWORD = "password"

def run_ilorest_test():
    print("--- Starting python-ilorest-library Test ---")
    
    try:
        # 1. Initialize the Redfish Client / 初始化 Redfish 客户端
        # Note: Set timeout and proxy if needed. Mock server is local.
        re_client = redfish.RedfishClient(
            base_url=SYSTEM_URL, 
            username=LOGIN_ACCOUNT, 
            password=LOGIN_PASSWORD
        )

        # 2. Login / 登录
        print(f"Attempting to login to {SYSTEM_URL}...")
        re_client.login(auth="session")
        print("Login successful!\n")

        # 3. Get System Information / 获取系统信息
        sys_path = "/redfish/v1/Systems/1"
        print(f"Fetching data from {sys_path}...")
        response = re_client.get(sys_path)
        
        if response.status == 200:
            data = response.dict
            print("Successfully retrieved System Information:")
            print(f"  - Model: {data.get('Model')}")
            print(f"  - Manufacturer: {data.get('Manufacturer')}")
            print(f"  - Health Status: {data.get('Status', {}).get('Health')}")
        else:
            print(f"Failed to fetch system data. Status: {response.status}")

        # 4. Get Power Information / 获取电源信息
        pwr_path = "/redfish/v1/Chassis/1/Power"
        print(f"\nFetching data from {pwr_path}...")
        response = re_client.get(pwr_path)
        
        if response.status == 200:
            pwr_data = response.dict
            # Match the structure from our mock-server
            pwr_control = pwr_data.get('PowerControl', [{}])[0]
            print("Successfully retrieved Power Information:")
            print(f"  - Power Consumed: {pwr_control.get('PowerConsumedWatts')} W")
        else:
            print(f"Failed to fetch power data. Status: {response.status}")

        # 5. Logout / 登出
        re_client.logout()
        print("\nLogout successful.")
        print("--- Test Completed Successfully ---")

    except Exception as e:
        import traceback
        print(f"\nERROR: An unexpected error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    run_ilorest_test()
