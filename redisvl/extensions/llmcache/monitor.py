import threading
import time
from typing import Optional
from redis import Redis
from redisvl.extensions.llmcache.semantic import SemanticCache

class CacheMonitor:
    def __init__(self,
                 redis_url: Optional[str] = "redis://localhost:6379",
                 semantic_cache: Optional[SemanticCache]=None
                 ):
        """
        Args:
            redis_url (Optiona[str]): The Redis url where the exists. Defaults to redis://localhost:6379
            semantic_cache (Optional[SemanticCache]): The semantic cache instance to monitor defaults is none and redis_url parameter will be used. 


        Raises:
            ConnectionError: if no semantic_cache is provided and redis_url is not a valid redis instance
        """

        # connect to the correct redis url

        # spin up a redis client handle so that cache metrics are stored
        # alongside the cache. Should re-use the same cache handle?

        # pull out the key-spaces, name-spaces, etc from cache that we should track

        # keep a handle of the cache to be able call things on it as needed

        # spin up a monitor that runs continually to listen to cache calls
        # ? is this blocking? ? can it run in one method while other methods
        # like `get_recall()` are called by user?

        # define methods to report overall metrics:
        # precision
        # recall
        # true positive
        # true negative
        # accuracy
        # F1 score
        # ROC, AUC

        # define methods to get specific document metrics like hit_count,
        # last_update_time, remaining_ttl, etc.
        
        # for metrics that we can't get from the Monitor patch the cache methods instead


        # IDEA: have an optimize() method that continually monitors one or more
        # of the above metrics and adjusts things like cosine similarity
        # automatically to tune parameters

        self._monitor = Redis().monitor()
        self.cache = semantic_cache
        self.counter = 0

    @property
    def hit_count(self):
        pass

    @property
    def true_positives(self):
        pass

    @property
    def true_negatives(self):
        pass

    @property
    def false_positives(self):
        pass

    @property
    def false_positives(self):
        pass

    def _incr_hit_count(self, key) -> None:
        pass

    def _patch_check(self): -> None:
        def new_check(self,
            prompt: Optional[str] = None,
            vector: Optional[List[float]] = None,
            num_results: int = 1,
        ) -> List[Dict[str, Any]]:

            if not (prompt or vector):
                raise ValueError("Either prompt or vector must be specified.")

            # Use provided vector or create from prompt
            vector = vector or self._vectorize_prompt(prompt)

            # Check for cache hits by searching the cache
            cache_hits = self._search_cache(vector, num_results, return_fields)
            for hit in cache_hits:
                self.client.incr(hit["key"]) ## set to pipeline
            return cache_hits

        import types
        funcType = types.MethodType
        self.cache.check = funcType(new_check, self.cache.check)

    
    ###################################
    ## experimenting
    def print_commands(self):
        print("in print_command")

        with self._monitor as monitor:
            print("in print_command with-block")
            for cmd in monitor.listen():
                print("in print_command with-block for-loop")
                print(cmd)
                self.counter += 1
                yield self.counter
                """
                yield 'working'
                """

    def check_for_command(self):
        if cmd := self._monitor.next_command():
            print(cmd)

    def check_next_command(self):
        cmd = next(self._monitor.listen())
        print(cmd)

    def start_and_stop(self):
        self.print_commands()
        # yield


