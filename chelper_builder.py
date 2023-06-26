#!/usr/bin/env python3

from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
    struct pull_history_steps {
        uint64_t first_clock, last_clock;
        int64_t start_position;
        int step_count, interval, add;
    };

    struct stepcompress *stepcompress_alloc(uint32_t oid);
    void stepcompress_fill(struct stepcompress *sc, uint32_t max_error
        , int32_t queue_step_msgtag, int32_t set_next_step_dir_msgtag);
    void stepcompress_set_invert_sdir(struct stepcompress *sc
        , uint32_t invert_sdir);
    void stepcompress_free(struct stepcompress *sc);
    int stepcompress_reset(struct stepcompress *sc, uint64_t last_step_clock);
    int stepcompress_set_last_position(struct stepcompress *sc
        , uint64_t clock, int64_t last_position);
    int64_t stepcompress_find_past_position(struct stepcompress *sc
        , uint64_t clock);
    int stepcompress_queue_msg(struct stepcompress *sc
        , uint32_t *data, int len);
    int stepcompress_extract_old(struct stepcompress *sc
        , struct pull_history_steps *p, int max
        , uint64_t start_clock, uint64_t end_clock);

    struct steppersync *steppersync_alloc(struct serialqueue *sq
        , struct stepcompress **sc_list, int sc_num, int move_num);
    void steppersync_free(struct steppersync *ss);
    void steppersync_set_time(struct steppersync *ss
        , double time_offset, double mcu_freq);
    int steppersync_flush(struct steppersync *ss, uint64_t move_clock);
""")

ffibuilder.cdef("""
    int32_t itersolve_generate_steps(struct stepper_kinematics *sk
        , double flush_time);
    double itersolve_check_active(struct stepper_kinematics *sk
        , double flush_time);
    int32_t itersolve_is_active_axis(struct stepper_kinematics *sk, char axis);
    void itersolve_set_trapq(struct stepper_kinematics *sk, struct trapq *tq);
    void itersolve_set_stepcompress(struct stepper_kinematics *sk
        , struct stepcompress *sc, double step_dist);
    double itersolve_calc_position_from_coord(struct stepper_kinematics *sk
        , double x, double y, double z);
    void itersolve_set_position(struct stepper_kinematics *sk
        , double x, double y, double z);
    double itersolve_get_commanded_pos(struct stepper_kinematics *sk);
""")

ffibuilder.cdef("""
    struct pull_move {
        double print_time, move_t;
        double start_v, accel;
        double start_x, start_y, start_z;
        double x_r, y_r, z_r;
    };

    struct trapq *trapq_alloc(void);
    void trapq_free(struct trapq *tq);
    void trapq_append(struct trapq *tq, double print_time
        , double accel_t, double cruise_t, double decel_t
        , double start_pos_x, double start_pos_y, double start_pos_z
        , double axes_r_x, double axes_r_y, double axes_r_z
        , double start_v, double cruise_v, double accel);
    void trapq_finalize_moves(struct trapq *tq, double print_time);
    void trapq_set_position(struct trapq *tq, double print_time
        , double pos_x, double pos_y, double pos_z);
    int trapq_extract_old(struct trapq *tq, struct pull_move *p, int max
        , double start_time, double end_time);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *cartesian_stepper_alloc(char axis);
    struct stepper_kinematics *cartesian_reverse_stepper_alloc(char axis);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *corexy_stepper_alloc(char type);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *corexz_stepper_alloc(char type);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *delta_stepper_alloc(double arm2
        , double tower_x, double tower_y);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *deltesian_stepper_alloc(double arm2
        , double arm_x);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *polar_stepper_alloc(char type);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *rotary_delta_stepper_alloc(
        double shoulder_radius, double shoulder_height
        , double angle, double upper_arm, double lower_arm);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *winch_stepper_alloc(double anchor_x
        , double anchor_y, double anchor_z);
""")

ffibuilder.cdef("""
    struct stepper_kinematics *extruder_stepper_alloc(void);
    void extruder_set_pressure_advance(struct stepper_kinematics *sk
        , double pressure_advance, double smooth_time);
""")

ffibuilder.cdef("""
    double input_shaper_get_step_generation_window(
        struct stepper_kinematics *sk);
    int input_shaper_set_shaper_params(struct stepper_kinematics *sk, char axis
        , int n, double a[], double t[]);
    int input_shaper_set_sk(struct stepper_kinematics *sk
        , struct stepper_kinematics *orig_sk);
    struct stepper_kinematics * input_shaper_alloc(void);
""")

ffibuilder.cdef("""
    #define MESSAGE_MAX 64
    struct pull_queue_message {
        uint8_t msg[MESSAGE_MAX];
        int len;
        double sent_time, receive_time;
        uint64_t notify_id;
    };

    struct serialqueue *serialqueue_alloc(int serial_fd, char serial_fd_type
        , int client_id);
    void serialqueue_exit(struct serialqueue *sq);
    void serialqueue_free(struct serialqueue *sq);
    struct command_queue *serialqueue_alloc_commandqueue(void);
    void serialqueue_free_commandqueue(struct command_queue *cq);
    void serialqueue_send(struct serialqueue *sq, struct command_queue *cq
        , uint8_t *msg, int len, uint64_t min_clock, uint64_t req_clock
        , uint64_t notify_id);
    void serialqueue_pull(struct serialqueue *sq
        , struct pull_queue_message *pqm);
    void serialqueue_set_wire_frequency(struct serialqueue *sq
        , double frequency);
    void serialqueue_set_receive_window(struct serialqueue *sq
        , int receive_window);
    void serialqueue_set_clock_est(struct serialqueue *sq, double est_freq
        , double conv_time, uint64_t conv_clock, uint64_t last_clock);
    void serialqueue_get_stats(struct serialqueue *sq, char *buf, int len);
    int serialqueue_extract_old(struct serialqueue *sq, int sentq
        , struct pull_queue_message *q, int max);
""")

ffibuilder.cdef("""
    void trdispatch_start(struct trdispatch *td, uint32_t dispatch_reason);
    void trdispatch_stop(struct trdispatch *td);
    struct trdispatch *trdispatch_alloc(void);
    struct trdispatch_mcu *trdispatch_mcu_alloc(struct trdispatch *td
        , struct serialqueue *sq, struct command_queue *cq, uint32_t trsync_oid
        , uint32_t set_timeout_msgtag, uint32_t trigger_msgtag
        , uint32_t state_msgtag);
    void trdispatch_mcu_setup(struct trdispatch_mcu *tdm
        , uint64_t last_status_clock, uint64_t expire_clock
        , uint64_t expire_ticks, uint64_t min_extend_ticks);
""")

ffibuilder.cdef("""
    void set_python_logging_callback(void (*func)(const char *));
    double get_monotonic(void);
""")

ffibuilder.cdef("""
    void free(void*);
""")

ffibuilder.set_source(
    "klippy._chelper",
    """
    #include "compiler.h"
    #include "itersolve.h"
    #include "list.h"
    #include "msgblock.h"
    #include "pollreactor.h"
    #include "pyhelper.h"
    #include "serialqueue.h"
    #include "stepcompress.h"
    #include "trapq.h"
    """,
    sources=[
        "src/chelper/itersolve.c",
        "src/chelper/kin_cartesian.c",
        "src/chelper/kin_corexy.c",
        "src/chelper/kin_corexz.c",
        "src/chelper/kin_delta.c",
        "src/chelper/kin_deltesian.c",
        "src/chelper/kin_extruder.c",
        "src/chelper/kin_polar.c",
        "src/chelper/kin_rotary_delta.c",
        "src/chelper/kin_shaper.c",
        "src/chelper/kin_winch.c",
        "src/chelper/msgblock.c",
        "src/chelper/pollreactor.c",
        "src/chelper/pyhelper.c",
        "src/chelper/serialqueue.c",
        "src/chelper/stepcompress.c",
        "src/chelper/trapq.c",
        "src/chelper/trdispatch.c",
    ],
    include_dirs=["src/chelper"]
)


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
