from glob import glob
import os
from typing import Dict, List, Optional, Tuple

import numpy as np

from .reader import DataReader


class M4Singer(DataReader):
    """M4Singer dataset loader.
    """
    SR = 44100

    def __init__(self, data_dir: str, sr: Optional[int] = None):
        """Initializer.
        Args:
            data_dir: dataset directory.
            sr: sampling rate.
        """
        self.sr = sr or M4Singer.SR
        self.speakers_, self.transcript = self.load_data(data_dir)

    def dataset(self) -> List[str]:
        """Return file reader.
        Returns:
            file-format datum reader.
        """
        return self.transcript

    def speakers(self) -> List[str]:
        """List of speakers.
        Returns:
            list of the speakers.
        """
        return self.speakers_

    def load_data(self, data_dir: str) -> Tuple[List[str], Dict[str, Tuple[int, str]]]:
        """Load audio.
        Args:
            data_dir: dataset directory.
        Returns:
            loaded data, speaker list, transcripts.
        """
        # generate file lists
        speakers, trans = os.listdir(data_dir), {}
        for sid, speaker in enumerate(speakers):
            for song in glob(os.path.join(data_dir, speaker, '*.wav')):
                path = song
                trans[path] = (sid, speaker)
        return speakers, trans
