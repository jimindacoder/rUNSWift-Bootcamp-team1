from BehaviourTask import BehaviourTask
from head.HeadCentre import HeadCentre
from head.HeadLocalise import HeadLocalise
from head.HeadtrackBall import HeadtrackBall
from util.GameStatus import GameState, GamePhase, game_state, game_phase
from util.Global import usingGameSkill, getCurrentSkill
from util.GameStatus import we_are_kicking_team, penalised



class MainHeadSkill(BehaviourTask):
    def _initialise_sub_tasks(self):
        self._sub_tasks = {
            "Centre": HeadCentre(self),
            "Localise": HeadLocalise(self),
            "Track": HeadtrackBall(self)
        }

    def _reset(self):
        self._current_sub_task = "Track"
        self._is_first_time_scan = True

    def _transition(self):
        if penalised():
            self._current_sub_task = "Centre"
            # Reset scan flag so it re-localizes after penalisation
            self._is_first_time_scan = True  
        else:
        # If unpenalised and first-time scan, perform wide scan for localisation
            if self._is_first_time_scan:
                self._current_sub_task = "Localise"
                self._is_first_time_scan = False
            else:
                # After the initial scan, switch to tracking the ball
                self._current_sub_task = "Track"
