import pdb
import time
import signal
import sys

def signal_handler(signal, frame):
    print("\nEntering debug mode...")
    pdb.set_trace()

# Attach signal handler for SIGINT (Interrupt from keyboard, usually Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

def main():
    # Your main code here
    while True:
        # Simulating a long-running process
        print("Running...")
        time.sleep(1)

if __name__ == "__main__":
    main()

