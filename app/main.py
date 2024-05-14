from streamlit.web.cli import main
import sys


if __name__ == "__main__":
    sys.argv = ["streamlit	", "run", "web.py", "--server.port=8501", "--server.address=0.0.0.0"]
    sys.exit(main(prog_name="streamlit"))
