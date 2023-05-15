import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
dosbox_exe = '/Applications/dosbox-x.app/Contents/MacOS/dosbox-x'

name = sys.argv[1]

zip_dir = Path('~/Games/Computer').expanduser()
zip_file = (zip_dir / name).with_suffix('.zip')
game_dir = HERE / name

if not game_dir.exists():
  print(f'Unzipping {zip_file} into {game_dir}')
  subprocess.run(['unzip', zip_file, '-d', game_dir])

subprocess.run([dosbox_exe, '-conf', 'dosbox.conf'], cwd=game_dir)
