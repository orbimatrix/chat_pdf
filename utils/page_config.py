from streamlit import set_page_config

from utils import version


def set():
    set_page_config(
        page_title="Notesgenie AI",
        page_icon="📄",
        menu_items={
            "About": f"NotesGeni AI\n "
            "\nDeveloper contact: saqibiqbal27772@gmail.com",
            
            "Get help": None,
        },
        layout="wide",
    )


if __name__ == "__main__":
    set()
