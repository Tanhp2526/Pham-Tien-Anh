class Environment:
    def execute_action(self, action: Action, args: dict) -> dict:
        """thực thi action và trả về kết quả."""
        try:
            res = action.execute(**args)
            return self.format_res(res)
        except Exception as e:
            return {
                "tool_executed":"False",
                "error" : str(e),
                "traceback": traceback.format_exc()
            }
        
    def format_res(self, res: Any) -> dict:
        """định dạng kết quả bằng metadata."""
        return {
            "tool_executed": True,
            "result" : res,
            "timestamp": time.strftime("%Y-%m-%dT%H:%s%z")
        }