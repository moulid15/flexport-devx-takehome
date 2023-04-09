"""
   Copyright 2023 Flexport International, LLC

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import random


def rock_paper_scissors(user_choice: int) -> int:
    """
    A Simple rock, paper scissors game.
    """
    # Generate computer choice
    pc_choice = random.randint(0, 2)
    if pc_choice == user_choice:  # pylint: disable=R1705
        return 0, pc_choice
    elif (user_choice + 1) % 3 == pc_choice % 3:
        return -1, pc_choice
    else:
        return 1, pc_choice

