from functions.exception_classes import InfoInconsistent

def validate_potential(potential, current):
    if current and potential and current != potential: 
        raise InfoInconsistent(f"potential {potential} != current {current}")
    else: 
        return