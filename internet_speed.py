import time
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # Convert from bits/s to Mbps
    upload = st.upload() / 1_000_000      # Convert from bits/s to Mbps
    ping = st.results.ping
    return download, upload, ping

if __name__ == "__main__":
        try:
            download, upload, ping = test_speed()
            print(f"Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps | Ping: {ping:.2f} ms")
        except Exception as e:
            print(f"Error: {e}")
        